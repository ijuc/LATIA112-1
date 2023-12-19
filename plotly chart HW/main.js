//Get data
d3.csv("https://raw.githubusercontent.com/ijuc/LATIA112-1/main/%E8%87%BA%E5%8C%97%E5%B8%82%E5%9C%8B%E6%B0%91%E4%B8%AD%E5%AD%B8%E5%83%91%E7%94%9F%E6%95%B8(E2).csv").then(
    res => {
        console.log(res);
        drawLineChart(res);
    }
);

function drawLineChart(res){
    let myGraph = document.getElementById("myGraph");
    let myGraph2 = document.getElementById("myGraph2");
    let myGraph3=document.getElementById('myGraph3');


    let trace1 = {};
    trace1.mode = "lines+markers";
    trace1.type = "scatter";
    trace1.name = "公立";
    trace1.marker = {
        size: 10
    };
    trace1.x = [];
    trace1.y = [];
    trace1.text = [];
    trace1.textposition = "bottom center";
    trace1.textfont = {
        family: "Raleway, sans-serif",
        size: 15,
        color: "blue"
    };

    for (let i = 0; i < res.length; i++) {
        trace1.x[i] = res[i]["years"];
        trace1.y[i] = res[i]["Municipal"];
        trace1.text[i] = res[i]["title"];
    }

    let trace2 = {};
    trace2.mode = "lines+markers";
    trace2.type = "scatter";
    trace2.name = "私立";
    trace2.marker = {
        size: 10
    };
    trace2.x = [];
    trace2.y = [];
    trace2.text = [];
    trace2.textposition = "bottom center";
    trace2.textfont = {
        family: "Raleway, sans-serif",
        size: 15,
        color: "blue"
    };

    for (let i = 0; i < res.length; i++) {
        trace2.x[i] = res[i]["years"];
        trace2.y[i] = res[i]["Private"];
        trace2.text[i] = res[i]["title"];
    }
    
    
    let data = [];
    data.push(trace1);
    data.push(trace2);


    let layout = {
        margin: {
            t: 80
        },
        title:"臺北市國民中學僑生數"


    
    };

    Plotly.newPlot(myGraph, data, layout);
    //  長條圖
    let trace3 = {
        type: 'bar',
        name: '僑生人數',
        x: [],
        y: [],
        text: [],
        textposition: "bottom center",
        textfont:{
            family: "Raleway, sans-serif",
            size: 15,
            color: "blue"
        }
    };

    for (let i =0; i <res.length; i++) {
        trace3.x[i] = res[i]['years'];
        trace3.y[i] = res[i]['Total'];
        trace3.text[i] = res[i]["title"];
    }

    let data2 =[trace3];
    let layout2 = {
        margin:{
            t:0
        },
        title:"僑生人數長條圖"
    };

    Plotly.newPlot(myGraph2, data2, layout2);
    //圓餅圖
    let aggregatedData = {};
    for (let i = 0; i < res.length; i++) {
        let category = res[i]['years'];
        let count = parseInt(res[i]['Total']);

       
        let commonPrefix = category.match(/^(.+?)\(/)?.[1] || category;

        if (aggregatedData[commonPrefix]) {
            aggregatedData[commonPrefix] += count;
        } else {
            aggregatedData[commonPrefix] = count;
        }
    }

    // Create data for the pie chart
    let trace4 = {
        type: 'pie',
        labels: Object.keys(aggregatedData),
        values: Object.values(aggregatedData),
        text: Object.keys(aggregatedData).map(category => `${category}<br>${aggregatedData[category]} 人`),
        hoverinfo: 'label+percent',
    };

    let data3 = [trace4];
    let layout3 = {
        margin: {
            t: 0
        },
        title: "僑生人數比例"
    };

    Plotly.newPlot(myGraph3, data3, layout3);
}
