const j = require("jimp");

j.read('data/melanoma/false/IMG_6712.png', (err, con) => {
    if (err) console.log(err);
    con.resize(30, 30).write("skin4.jpg");
    // So this will reopen it and resize it. I'm just not sure if I'll lose important information in the process.
})