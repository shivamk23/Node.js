const http = require("http");
const fs=require("fs");
const server=http.createServer((req,res)=>{
    // console.log (req.url);
    if(req.url=="/"){
        res.setHeader("Content-Type","text/html");
        fs.readFile("./index.html","UTF-8",(err,data)=>{
            if(err){
                console.log(err)
            }else{
                res.end(data)
            }
        })
        
    }
    else if(req.url=="/about"){
        res.setHeader("Content-Type","text/html");

        fs.readFile("./about.html","UTF-8",(err,data)=>{
            if(err){
                console.log(err);
            }else
            
            {  
                res.end(data)
            }
        })
    }
    else{
        res.end();
    }
})
server.listen(3000,(err)=>{
    if(err)
    console.log("Error in started server");
    else
    console.log("Server started");
})