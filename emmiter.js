const EventEmitter=require("events");
const event = new EventEmitter();
// event.on('CLicked',function(e){
//     console.log(`Button clicked `);
// })
// class loger extends EventEmitter{
//  log(){
//     console.log("Message from function");
//     event.emit("Clicked");
// }}
// module.exports=loger;
const mycode=require("./emmiter1");
mycode.event.on("Logged",()=>{
    console.log("Event handled");
})

mycode.log();