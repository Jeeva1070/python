const express = require('express');
const bodyParser = require('body-parser');
const chatbot = require('./chatbot');

const app = express();
app.use(bodyParser.json());

app.post('/chatbot', (req, res) => {
    const user_input = req.body.user_input;
    const response = chatbot.getResponse(user_input);
    res.json({ response: response });
});

app.listen(3000, () => {
    console.log('Server running on port 3000');
});