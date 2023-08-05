const fs=require("fs");
//const contents=fs.readFileSync("./path.js","utf-8");
// fs.readFile("./path.js","utf-8",function(err,data){
//     if(err)
//     console.log("unable to read file");
//     else
//     console.log(data);

// })

fs.writeFile("./data.txt","Demo data",function(err){
    if(err)
    console.log("Unable to write data");
    else
    console.log("Data written");

});

// fs.readdir("./",function(err,contents){
//     console.log(contents);
// })
//console.log(contents);
