$(document).ready(function() {
    // When a checklist is clicked
    $('.checklist-link').click(function() {
        let checklistId = $(this).data('id');

        // Make an AJAX request to fetch the tasks for the selected checklist
        $.ajax({
            url: '/checklist/' + checklistId + '/tasks/', // Your URL pattern for fetching tasks
            method: 'GET',
            success: function(response) {
                $('#task-list-container').html(response);
            }
        });
    });

    // When the status dropdown is changed
    $('.task-status').change(function() {
        let taskId = $(this).data('task-id');
        let status = $(this).val();

        // Make an AJAX request to update the task status
        $.ajax({
            url: '/task/' + taskId + '/update-status/', // Your URL pattern for updating task status
            method: 'POST',
            data: {
                'status': status,
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()
            },
            success: function(response) {
                alert('Task status updated!');
            }
        });
    });
})