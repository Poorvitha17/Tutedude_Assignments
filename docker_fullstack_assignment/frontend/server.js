const express = require("express");
const path = require("path");

const app = express();
const PORT = 3000;

const BACKEND_URL =
    process.env.BACKEND_URL || "http://localhost:5000";

app.use(express.urlencoded({ extended: true }));

app.use(express.static(path.join(__dirname, "public")));

app.post("/submit", async (req, res) => {
    try {
        const studentData = {
            name: req.body.name,
            course: req.body.course
        };

        const response = await fetch(`${BACKEND_URL}/submit`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(studentData)
        });

        const result = await response.json();

        if (!response.ok) {
            return res.status(response.status).send(
                `Error: ${result.error}`
            );
        }

        res.send(`
            <h2>Submission Successful!</h2>
            <p>Name: ${result.data.name}</p>
            <p>Course: ${result.data.course}</p>
        `);

    } catch (error) {
        res.status(500).send(
            `Unable to connect to Flask backend: ${error.message}`
        );
    }
});

app.listen(PORT, () => {
    console.log(`Frontend running on port ${PORT}`);
});