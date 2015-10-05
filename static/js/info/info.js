/**
 * Created by dfitzgerald on 9/25/15.
 */
var animationEnd = 'webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend';
var reportId = 0;

function getCards(cardNames, colAttach, animated){
    /* Get column to load cards into */
    var $infoCol = $('#info-col-' + colAttach);

    /* Get card data */
    $.get('/viewer/cards/' + reportId + '/', {cards: cardNames}, function(data){
        var $cards = $(data).find('.igsbviewer-card');
        for(var i = 0; i < $cards.length; i++){
            /* Load cards in the same order as parameter cardNames */
            var $newCard = $cards.filter('.igsbviewer-card[data-name="' + cardNames[i] + '"]')
                .addClass(animated ? 'animated fadeInUp': '')
                .appendTo($infoCol);
            /* Attach event handler for sliding up card contents */
            $newCard.find('div.igsbviewer-card-heading').first().click(function(){
                $(this).siblings().slideToggle(200);
            });
            /* This is a special case and shouldn't stay here TODO */
            //$newCard.find('.variant').click(function(){
            //    clearCards('right', true);
            //    window.setTimeout(function(){
            //        clearCards('left', true, function(){
            //            getCards(['studyDescription', 'barchart', 'sample2'], 'left', true);
            //            window.setTimeout(function(){
            //                getCards(['chart', 'samplesDescription', 'sample2', 'sample1'], 'right', true)
            //            }, 200);
            //        });
            //    }, 200);
            //});

            /* If card contains a chart, load chart data */
            if($newCard.data('chart-name') !== undefined){
                var chartName = $newCard.data('chart-name');
                var chartKwargs = JSON.stringify($('i.chart-vars').first().data());
                if(chartKwargs === undefined){
                    chartKwargs = '{}';
                }
                $.getJSON('/viewer/get_series_data/', {
                    chartName: chartName,
                    chartKwargs: chartKwargs
                },function(dataJSON){
                    var $chartCard = $infoCol.find('div.igsbviewer-card[data-chart-name="' + dataJSON.chart_name + '"]');
                    $chartCard.find('div.igsbviewer-card-chart').first().highcharts(dataJSON.highchart);
                });
            }
        }
    });
}

function clearCards(colAttach, animated, callback){
    var $infoCol = $('#info-col-' + colAttach);
    var def = new $.Deferred();
    $infoCol.find('div.igsbviewer-card')
        .removeClass('animated fadeInUp')
        .addClass('animated fadeOutDown')
        .one(animationEnd, function(){
            $(this).remove();
            def.resolve();
        });
    $.when(def).done(function(){
        if(callback !== undefined) callback();
    });
}


$(document).ready(function(){
    reportId = $('#report-id').data('report-id');
    /* Set Highcharts default options */
    Highcharts.setOptions({
        credits: {
            enabled: false
        }
    });

    //$.getScript('/viewer/js/info/cards.js');

    /* Load initial set of cards */
    getCards(['reportSummary', 'geneList'], 'sidebar', false);
    //getCards(['topfivegenes'], 'span-both', true);
    getCards(['studyDescription', 'topfivegenes', 'sample2'], 'left', true);
    window.setTimeout(function(){
        getCards(['effectratio', 'refalleleratio', 'samplesDescription', 'sample2', 'sample1'], 'right', true)
    }, 200);
});