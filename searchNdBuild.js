const fs= require('fs');


//this is the synchronus function 
// const data=fs.readFileSync("./path.js","utf-8");
// console.log(data);

//this is the asynchronus function
// const data =fs.readFile("./path.js","utf-8",function(err,data){
//     if(err){
//         console.log("unable to read file");
//     }
//     else
//     console.log(data)
// })

//this is the write function
// fs.writeFile("./pathstxt","all paths",function(err){
//     if(err)
//     {
//         console.log("Not able to write")
//     }
//     else{
//         console.log("Written")
//     }
// });

//this is the read directory function
// fs.readdir("./",function(err,data){
//     if(err){
//         console.log("unable to found")
//     }else{
//         console.log(data)
//     }
// })

//this is the append function
// fs.appendFile("./paths.txt","all path",function(err){
//     if(err)
//     {
//         console.log("Not able to write")
//     }
//     else{
//         console.log("Written")
//     }
// });

//this is the unlink function
// fs.unlink("./data.txt",function(err){
//     if(err)
//     {
//         console.log("Not able to write")
//     }
//     else{
//         console.log("Written")
//     }
// });


//this is the rename function
// fs.rename("./path.txt","./paths.txt",function(err){
//     if(err)
//     {
//         console.log("Not able to write")
//     }
//     else{
//         console.log("Written")
//     }
// });

//this is the search for js files and add file path in paths.txt file
function search(path){
fs.readdir(path,function(err,files){
    if(!err){
        files.forEach((item)=>{
            if(item.endsWith(".js")){
                fs.appendFile("./paths.txt",path+'/'+item+"\n",function(err){
                    if(err){
                        console.log("Somthing issue")
                    }else{
                        console.log("Witten files")
                    }
                })
                
            }
            search(path+"/"+item);
        })
    }
})
}
search('.');
//search("/Users/admin"); //replace with your directory name or any other folder you want


