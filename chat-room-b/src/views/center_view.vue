<template>
    <div>
        <h1>Realtime communication with WebRTC</h1>

        <video id="localVideo" autoplay playsinline></video>
        <video id="remoteVideo" autoplay playsinline></video>

        <div>
            <button id="startButton" @click="startAction">开始</button>
            <button id="callButton" @click="callAction">调用</button>
            <button id="hangupButton" @click="link">挂断</button>
        </div>
    </div>
</template>
<script>
import Cookies from "js-cookie";
import { init } from "@/utils/webSocket.js";
export default {
    data: function () {
        return {
            localStream: "",
            socket_my: "",
            localPeerConnection: "",
            remotePeerConnection: "",
        };
    },
    mounted() {
        this.socket_my = init("test");
        this.socket_my.onmessage = (res) => this.receiveWebSocket(res);
    },
    methods: {
        sendWebSocket(message) {
            this.socket_my.send(JSON.stringify(message));
        },
        receiveWebSocket(res) {
            let data = JSON.parse(res.data);
            console.log(data);
            console.log(typeof data);
            console.log(data["act"] === "description_offer");
            if (data["act"] === "message") {
                console.log(res.data["message"]);
            } else if (data["act"] === "description_offer") {
                this.remotePeerConnection = new RTCPeerConnection();
                console.log("3远端加载本地description");
                this.remotePeerConnection.setRemoteDescription(
                    data["description"]
                );
                this.remotePeerConnection.addEventListener(
                    "icecandidate",
                    this.remoteHandleConnection
                );
                this.remotePeerConnection.ontrack = ({ streams: [stream] }) => {
                    remoteVideo.srcObject = stream;
                };
                console.log("4远端创建answer");
                this.remotePeerConnection
                    .createAnswer() // 第四步，远端创建answer，生成远端description
                    .then(this.createdAnswer);
            } else if (data["act"] === "description_answer") {
                console.log("6本地加载远端description");
                this.localPeerConnection.setRemoteDescription(
                    data["description"]
                );
            } else if (data["act"] === "ic_offer") {
                console.log("9远端加载本地ic");

                this.remotePeerConnection.addIceCandidate(
                    new RTCIceCandidate(data["ic"])
                );
            } else if (data["act"] === "ic_answer") {
                console.log("10本地加载远端ic");
                console.log(data);
                this.localPeerConnection.addIceCandidate(
                    new RTCIceCandidate(data["ic"])
                );
            } else {
                console.log(res);
            }
        },
        link() {
            const message = {
                act: "init",
                user_name: Cookies.get("user_name"),
            };
            this.sendWebSocket(message);
        },
        startAction() {
            const mediaStreamConstraints = {
                video: true,
                audio: false,
            };
            navigator.mediaDevices
                .getUserMedia(mediaStreamConstraints)
                .then(this.gotLocalMediaStream);
        },
        gotLocalMediaStream(mediaStream) {
            // 加载本地视频流
            localVideo.srcObject = mediaStream;
            this.localStream = mediaStream;
            callButton.disabled = false;
        },

        hangupAction() {
            // localPeerConnection.close();
            // remotePeerConnection.close();
            // localPeerConnection = null;
            // remotePeerConnection = null;
            hangupButton.disabled = true;
            callButton.disabled = false;
        },
        callAction() {
            const videoTracks = this.localStream.getVideoTracks();
            const audioTracks = this.localStream.getAudioTracks();

            this.localPeerConnection = new RTCPeerConnection(null);

            this.localPeerConnection.addEventListener(
                "icecandidate",
                this.loaclHandleConnection
            );

            this.localStream.getTracks().forEach((track) => {
                this.localPeerConnection.addTrack(track, this.localStream);
            });

            const offerOptions = {
                offerToReceiveVideo: 1,
                // offerToReceiveAudio: 1,
            };
            console.log("1创建offer");
            this.localPeerConnection
                .createOffer(offerOptions)
                .then(this.createdOffer);
        },
        localHandleConnection(event) {
            const iceCandidate = event.candidate;

            if (iceCandidate) {
                console.log("7本地加载远端description完成，向远端发送ic");
                // const newIceCandidate = new RTCIceCandidate(iceCandidate);
                this.$store.dispatch("req", {
                    url: "/ic_offer",
                    data: {
                        ic: iceCandidate,
                        user_from: "jl",
                        user_to: "jl01",
                    },
                });
            }
        },
        remoteHandleConnection(event) {
            const iceCandidate = event.candidate;

            if (iceCandidate) {
                console.log("8远端加载本地description完成，向本地发送ic");
                // const newIceCandidate = new RTCIceCandidate(iceCandidate);
                this.$store.dispatch("req", {
                    url: "/ic_answer",
                    data: {
                        ic: iceCandidate,
                        user_from: "jl01",
                        user_to: "jl",
                    },
                });
            }
        },
        createdOffer(description) {
            console.log("2本地set本地description");
            this.localPeerConnection.setLocalDescription(description);
            this.$store.dispatch("req", {
                url: "/description_offer",
                data: {
                    description: description,
                    user_from: "jl",
                    user_to: "jl01",
                },
            });
        },

        createdAnswer(description) {
            console.log("5远端加载远端description");
            this.remotePeerConnection.setLocalDescription(description);

            this.$store.dispatch("req", {
                url: "/description_answer",
                data: {
                    description,
                    user_from: "jl01",
                    user_to: "jl",
                },
            });
        },
    },
};
</script>

