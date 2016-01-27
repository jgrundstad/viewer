$(document).ready(function(){
    $('#search').click(function(){
        /* Get handles, hide any existing event icons, show spinner */
        var $table_container = $('#table_container');
        var $loading_cloud = $('#loading_cloud');
        $table_container.hide();
        $('.event_icon').hide();

        /* Get search values, construct request url */
        var searchCol = $('#search_col_select').val();
        var searchTerm = $('#search_box').val();
        var searchType = $('#search_type_select').val();
        var requestUrl = '/viewer/ajax_search_reports/' + searchCol
                + '/' + searchTerm + '/' + searchType + '/';

        /* Check to make sure user input isn't blank
         * If it is, the ajax call won't be correctly routed
         * and nothing will happen
         */
        if(searchTerm === ''){
            $('#error_user').show()
                    .children('span').addClass('shake');
            return null;
        }

        /* Show loading cloud */
        $loading_cloud.show();

        var reportIds = [];
        $('.multiplereports').filter(':checked').each(function(){
            reportIds.push($(this).data('reportid'));
        });

        var searchPostData = {};
        if(reportIds.length > 0){
            searchPostData.report_ids = JSON.stringify(reportIds);
        }

        /* Make ajax call */
        $.post(requestUrl, searchPostData, function(data){
            /* Run function once data is received */
            $loading_cloud.hide();
            if(true/*data.status >= 200 && data.status < 300*/){
                $table_container.empty().show();
                /* If content came back empty, report no results to user */
                if(data/*.content*/ === ''){
                    $('#no_results').show().children('span').addClass('pulse');
                }else{
                    /* If content came back, format into DataTable */
                    //console.log(data);
                    var table_id = 'report-table';
                    var $result_table = $(data/*.content*/).prop({
                        'class': 'table table-hover',
                        'id': table_id
                    }).appendTo('#table_container');
                    //$result_table.DataTable({
                    //    scrollY: 400,
                    //    scrollX: true,
                    //    autowidth: false,
                    //    scrollCollapse: true,
                    //    paging: false,
                    //    "dom": 'RC<"clear">lfrtip'
                    //});
                    //
                    ///* A little visual formatting so it's visually consistent */
                    //var $result_table_wrapper = $('#' + table_id + '_wrapper');
                    //$result_table_wrapper.find('input[type="search"]')
                    //        .addClass('form-control')
                    //        .css({
                    //            'display': 'inline',
                    //            'width': 'inherit'
                    //        });
                    //$result_table_wrapper.find('button.ColVis_Button')
                    //        .removeClass('ColVis_Button ColVis_MasterButton')
                    //        .addClass('btn btn-sm btn-primary')
                    //        .css('margin-left', '0.5em');
                }

                var newWindowHtml = $('#search-data-area').html();
                console.log(newWindowHtml)
                var w = window.open();
                w.document.writeln(newWindowHtml);
            }else{
                /* If status code was not 2xx, report server error to user */
                $('#error_server').show()
                        .children('span.animated').addClass('hinge');
            }
        });
    });

    /* Search on Enter press */
    $(document).keypress(function(e){
        if(e.which == 13 && $('#search_box').is(':focus')){
            $('#search').click();
        }
    });
});