/**
 * Created by Dominic Fitzgerald on 10/5/15.
 */

$(document).ready(function(){
    console.log('deferred');
    $('.variant').click(function(){
        clearCards('right', true);
        window.setTimeout(function(){
            clearCards('left', true, function(){
                getCards(['studyDescription', 'barchart', 'sample2'], 'left', true);
                window.setTimeout(function(){
                    getCards(['chart', 'samplesDescription', 'sample2', 'sample1'], 'right', true)
                }, 200);
            });
        }, 200);
    });
});