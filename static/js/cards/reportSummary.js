/**
 * Created by Dominic Fitzgerald on 10/5/15.
 */
$(document).ready(function(){

    $('.report-view-btn').click(function(){
        clearActiveAndGetOffset(['studyDescription', 'topfivegenes', 'sample2'], {},
            ['effectratio', 'samplesDescription', 'sample2', 'sample1'], {});
    }).click();

    $('.gene-view-btn').click(function(){
        clearActiveAndGet(['geneList'], 'span-both', {})
    });
});