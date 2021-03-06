var stub_data = "[[1344816000, 3184.12088], [1344902400, 3182.169974], [1344988800, 3193.98483], [1345075200, 3180.151921], [1345161600, 3186.048728], [1345420800, 3172.999415], [1345507200, 3186.447201], [1345593600, 3182.688039], [1345680000, 3182.909557], [1345766400, 3189.329126]]";
var IMA = {};

var Flotr = Flotr || {};

IMA.drawChart = function() {
    var container = document.getElementById("container");

    // var data = JSON.parse(stub_data);

    $.getJSON('/assets/IMA-B%20TOTAL/data', function(data) {
        Flotr.draw(container, {series:{data: data}}, {
            HtmlText : false,
            title: "IMA Historic",
            xaxis: {
                labelsAngle: 45,
                mode: "time",
                timeFormat: "%d %b",
                timeMode: "local",
                timeUnit: "second",
                noTicks: $(container).width()/50
            },
            yaxis: {
                tickFormatter: function(n) { return parseInt(n) }
            }
        });
    });
};

IMA.drawChart();
