$(function spark_item_hover() {
    $(this).on('mouseenter.collapse.data-api', '[data-toggle=collapse]', function() {
        var $this = $(this), target = $this.attr('data-target')
        , option = $(target).data('collapse') ? 'show' : $this.data()
        $(target).collapse();
        $(target).show('true');
    })
    $(this).on('mouseleave.collapse.data-api', '[data-toggle=collapse]', function() {
        var $this = $(this), target = $this.attr('data-target')
        , option = $(target).data('collapse') ? 'hide' : $this.data()
        $(target).hide('true');
    })   
})


