add_name_and_link_habit_in_model_delete()

function add_name_and_link_habit_in_model_delete(){
    
    var button_delete_all = document.querySelectorAll(".button_delete")

    button_delete_all.forEach(function(button_delete){
        button_delete.addEventListener("click", function(){
            
            var button_in_modal_name_habit = button_delete.querySelector(".in_modal_name_habit")
            var button_in_modal_link_habit = button_delete.querySelector(".in_modal_link_habit")

            var in_modal_name_habit = button_in_modal_name_habit.cloneNode(true)
            var in_modal_link_habit = button_in_modal_link_habit.cloneNode(true)


            in_modal_name_habit.classList.remove("invisible")
            in_modal_link_habit.classList.remove("invisible")


            var modal_body = document.querySelector(".modal-body")
            var btn_primary = document.querySelector(".btn-primary")

            var already_exist_in_modal_name_habit = modal_body.querySelector(".in_modal_name_habit")
            var already_exist_in_modal_link_habit = btn_primary.querySelector(".in_modal_link_habit")

            
            if(already_exist_in_modal_name_habit)
                already_exist_in_modal_name_habit.remove()
            if(already_exist_in_modal_link_habit)
                already_exist_in_modal_link_habit.remove()

            modal_body.appendChild(in_modal_name_habit)
            btn_primary.appendChild(in_modal_link_habit)


        })
    })
}