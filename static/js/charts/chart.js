/**
 * Created by dfitzgerald on 9/28/15.
 */
var $chartCard = $('div.igsbviewer-card[data-name="chart"]');
var chartName = $chartCard.data('chart-name');
$.getJSON('/viewer/get_series_data/' + chartName + '/', function(dataJSON){
    $('div.igsbviewer-card[data-name="chart"]').find('.igsbviewer-card-content').first().highcharts({
        credits: {
            enabled: false
        },
        chart: {
            type: 'pie'
        },
        title: {
            text: 'Fruit Consumption'
        },
        xAxis: {
            categories: ['Apples', 'Pears', 'Strawberries']
        },
        yAxis: {
            title: {
                text: 'Fruit Eaten'
            }
        },
        series: [
            dataJSON
        ]
    });
});


console.log(document.currentScript);
