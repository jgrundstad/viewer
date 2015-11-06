/**
 * Created by Dominic Fitzgerald on 10/5/15.
 */

$(document).ready(function(){
    $('.gene-name3').click(function(){
        var gene_name = $(this).data('name');
        console.log(gene_name);
        clearActiveAndGet(['geneProfile'], 'span-both', {gene_name: gene_name});
    })
});