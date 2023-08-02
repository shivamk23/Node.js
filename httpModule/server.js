const http=require("http");
// console.log(http)
const server=http.createServer();
server.on("connection",()=>{
    console.log("Connection req..")
})
server.listen(3000);