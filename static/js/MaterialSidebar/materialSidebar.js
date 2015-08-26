/**
 * Created by dfitzgerald on 8/21/15.
 */
(function($){

$.widget('djf604.MaterialSidebar', {
    options: {
        toggleSelector: ''
    },

    /* Define instance variables */
    $sidebarContainer: null,
    $sidebarOverlay: null,

    /* Constructor */
    _create: function(){
        var widget = this;
        widget.$sidebarContainer = widget.element;

        widget.$sidebarOverlay = $('<div>').addClass('sidebar-overlay').click(function(){
            $(this).removeClass('active');
            widget.$sidebarContainer.removeClass('open');
        });
        widget.$sidebarOverlay.appendTo($('body'));


        /* Match dropdown elements to targets */
        widget.$sidebarContainer.find('[data-target]').each(function(){
            var targetId = $(this).data('target');
            console.log('target is: ' + targetId);
            $(this).click(function(){
                $(targetId).stop(true, true).slideToggle();
            });
        });

        /* Attach toggle handle */
        $(widget.options.toggleSelector).click(function(){
            console.log('opened');
            widget.open();
        });
    },

    open: function(){
        var widget = this;
        widget.$sidebarContainer.toggleClass('open');
        if ((widget.$sidebarContainer.hasClass('sidebar-fixed-left')
            || widget.$sidebarContainer.hasClass('sidebar-fixed-right'))
            && widget.$sidebarContainer.hasClass('open')) {
            widget.$sidebarOverlay.addClass('active');
        } else {
            widget.$sidebarOverlay.removeClass('active');
        }
        console.log('workied');
    }
});

})(jQuery);