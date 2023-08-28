const http=require("http")
const fs=require("fs");

const server=http.createServer(handlereq);
function handlereq(req,res){
    if(req.url=="/"){
        res.write(readData("./index.html"))
        res.end();
    }
    else {
    try{
        console.log((req.url.substr(1)))
        res.write(readData(req.url.substr(1)))
        res.end();
    }catch(e){
        res.end();
    }
}
}
server.listen(3000,(err)=>{
if(err){
    console.log("there is an error in Starting server...")
}else{
    console.log("Server Started at port 3000")
}
})
function readData(filename){
    let content= fs.readFileSync(filename,"UTF-8");
    return content;
}