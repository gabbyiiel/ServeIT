// handle selection change event for college drop-down menu
document.querySelector("#college").addEventListener("change", function() {
  // get selected college
  var college = this.value;

  // update options for course drop-down menu based on selected college
  updateCourseOptions(college);
});

// update options for course drop-down menu
function updateCourseOptions(college) {
  // get course drop-down menu
  var courseSelect = document.querySelector("#courses");

  // clear existing options
  courseSelect.innerHTML = "";

  // add options based on selected college
  if (college == "College of Computer Studies") {
    courseSelect.innerHTML += "<option value='BSCS'>BSCS</option>";
    courseSelect.innerHTML += "<option value='BSIT'>BSIT</option>";
    courseSelect.innerHTML += "<option value='BSDA'>BSDA</option>";
  } else if (college == "CSM") {
    courseSelect.innerHTML += "<option value='BSME'>BSME</option>";
    courseSelect.innerHTML += "<option value='BSIE'>BSIE</option>";
  }else if (college == "") {
    courseSelect.innerHTML += "<option selected disabled value=>Select College</option>";

  }
  else {
    // add default option
    courseSelect.innerHTML += "<option value=''></option>";
  }

}