const express = require("express");
const app = express();
const axios = require("axios");
const cassandra = require("cassandra-driver");
const bodyParser = require("body-parser");

app.use(express.json());
app.use(bodyParser.urlencoded({ extended: true }));

const client = new cassandra.Client({
  contactPoints: ["192.168.1.219", "192.168.1.220"],
  localDataCenter: "datacenter1",
  keyspace: "weather",
  credentials: { username: "cassandra", password: "cassandra" },
});

app.get("/", function (req, res) {
  const query = `
    CREATE TABLE emp(
        emp_id int PRIMARY KEY,
        emp_name text,
        emp_city text,
        emp_sal varint,
        emp_phone varint
        );
    `;
  client.execute(query, []).then((result) => console.log(result));
});

app.post("/add-report", async (req, res) => {
  let lat = req.body.lat;
  let long = req.body.lon;

  // console.log(req.body);
  let body = {};

  axios
    .get(
      `https://api.openweathermap.org/data/2.5/onecall?lat=${lat}&lon=${long}&exclude=minutely,hourly,daily&appid=4fc57c093b1962e1f5db11a8b893119c`
    )
    .then((response) => {
      let data = response.data;
      body["id"] = data["current"]["sunrise"];
      body["lat"] = data["lat"];
      body["long"] = data["lon"];
      body["dt"] = data["current"]["dt"];
      body["temp"] = data["current"]["temp"];
      body["windspeed"] = data["current"]["wind_speed"];

      const query = `
        insert into weather.weatherinfo(
            id, dt, lat, long, temp, windspeed
        ) values(
            '${String(body["id"])}', '${String(body["dt"])}', '${String(
        lat
      )}', '${String(long)}', '${String(body["temp"])}', '${String(
        body["windspeed"]
      )}'
        );
        `;

      client.execute(query, []).then((result) => console.log(result));

      return res.status(201).json({
        message: "Added Successfully!",
      });
    })
    .catch((err) => {
      console.log(err);
      return res.status(500).json({
        message: "Some Error Occurred!",
      });
    });
});

app.get("/all-reports", async (req, res) => {
  let theRequired = [];
  const query = `
        select * from weather.weatherinfo;
        `;
  client
    .execute(query, [])
    .then((result) => {
      return res.json(result.rows);
    })
    .catch((err) => {
      console.log(err.message);
    });
});

app.listen(3000, () => {
  console.log("server is running on port 3000");
});
