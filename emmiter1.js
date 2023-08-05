const EventEmitter=require("events");
const event = new EventEmitter();

function log(){
    console.log("Workng on log");
    event.emit("Logged");
}

module.exports=log;
module.exports.event=event;