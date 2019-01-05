const j = require("jimp");

j.read('blue.jpg', (err, con) => {
    if (err) console.log(err);
    con.resize(256, 256).write("see.jpg");
    // So this will reopen it and resize it. I'm just not sure if I'll lose important information in the process.
})