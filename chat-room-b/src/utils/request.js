import axios from 'axios'

const req = axios.create({
    method: "post",
    baseURL: "http://127.0.0.1:8000/",
    timeout: 10000,
})

export default req