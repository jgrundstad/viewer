/**
 * Created by Dominic Fitzgerald on 10/5/15.
 */
$(document).ready(function(){

    $('.report-view-btn').click(function(){
        clearActiveAndGetOffset(['topfivegenes'], {},
            ['qualitative_map', 'effectratio'], {});
    }).click();

    $('.gene-view-btn').click(function(){
        clearActiveAndGet(['geneList'], 'span-both', {})
    });
});