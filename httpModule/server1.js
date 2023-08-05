const http=require("http");
const fs=require("fs");
function readAndServe(path){

    return fs.readFileSync(path,"UTF-8")
}

const server=http.createServer((req,res)=>{
    let url=req.url;
    let method=req.method;
    if(url=="/" && method=="GET"){
        let data=readAndServe("./index.html");
        res.end(data);
    }else if(url==="/about" && method==="GET"){
        let data=readAndServe("./about.html");
        res.end(data);

    }else if(url==="/contact" && method==="GET"){
        let data=readAndServe("./contact.html");
        res.end(data);
    }else{
        res.end("Not found...");
    }
});

server.listen(3000);

