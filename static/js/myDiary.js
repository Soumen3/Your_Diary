console.log("My Diary");


document.addEventListener(('DOMContentLoaded'), () => {
	const dialog = document.querySelector('#delete-todo-dialog');
	const openDialogButton = document.querySelectorAll('.delete-btn');
	const closeDialogButton = document.querySelector('#closeDialog');

	console.log(openDialogButton);
	
	openDialogButton.forEach(function(button) {
		button.addEventListener('click', function(e) {
			e.preventDefault();
			dialog.showModal();
		});
	});

	// openDialogButton.addEventListener('click', () => {
	// 	dialog.showModal();
	// });

	closeDialogButton.addEventListener('click', (e) => {
		e.preventDefault();
		dialog.close();
	});


	document.querySelectorAll('.delete-btn').forEach(function(button) {
		console.log(button);
		
		button.addEventListener('click', function() {
			var pageId = this.getAttribute('data-id');
			var form = document.querySelector('.delete-todo-form');

			form.action = `delete-page/${pageId}/`;
		});
	});
});