/**
 * Created by dfitzgerald on 9/25/15.
 */
var animationEnd = 'webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend';
var reportIds = [];

function getCards(cardNames, colAttach, animated, cardVars){
    /* Get column to load cards into */
    var $infoCol = $('#info-col-' + colAttach);
    $infoCol.data('active', 'active');

    /* Get card data */
    if(cardVars === undefined) cardVars = {};
    cardVars.cards = cardNames;
    cardVars.report_ids = reportIds;
    $.get('/viewer/cards/get/', cardVars, function(data){
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

function getCardsOffset(cardNamesLeft, cardVarsLeft, cardNamesRight, cardVarsRight){
    getCards(cardNamesLeft, 'left', true, cardVarsLeft);
    window.setTimeout(function(){
        getCards(cardNamesRight, 'right', true, cardVarsRight);
    }, 200);
}

function clearCardsCol(colAttach, animated, callback){
    var $infoCol = $('#info-col-' + colAttach);
    $infoCol.data('active', 'inactive');
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

function clearCardsOffset(finalCallback){
    clearCardsCol('right', true);
    window.setTimeout(function(){
        clearCardsCol('left', true, finalCallback);
    }, 200);
}

function clearCardsActive(finalCallback){
    if($('#info-col-span-both').data('active') === 'active'){
        clearCardsCol('span-both', true, finalCallback);
    }else if($('#info-col-left').data('active') === 'active'
             && $('#info-col-right').data('active') === 'active'){
        clearCardsOffset(finalCallback);
    }else{
        if(finalCallback !== undefined) finalCallback();
    }
}

function clearActiveAndGetOffset(cardNamesLeft, cardVarsLeft, cardNamesRight, cardVarsRight){
    clearCardsActive(function(){
        getCardsOffset(cardNamesLeft, cardVarsLeft, cardNamesRight, cardVarsRight);
    });
}

function clearActiveAndGet(cardNames, col, cardVars){
    clearCardsActive(function(){
        getCards(cardNames, col, true, cardVars);
    })
}

$(document).ready(function(){
    reportIds = $('#report-ids').data('report-ids');

    /* Set Highchars global defaults */
    Highcharts.setOptions({
        credits: {
            enabled: false
        }
    });

    /* Load initial set of cards */
    if(reportIds.length > 1){
        getCards(['reportMultiple'], 'sidebar', false);
    }else{
        getCards(['reportSummary'], 'sidebar', false);
    }


});