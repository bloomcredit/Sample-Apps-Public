/**
 * Validates the form based on required fields/required patterns
 */
document.addEventListener("DOMContentLoaded", () => {
  const forms = document.querySelectorAll(".needs-validation");

  forms.forEach((form) => {
    form.addEventListener("submit", (event) => {
      if (!form.checkValidity()) {
        event.preventDefault();
        event.stopPropagation();
      } else {
        showLoading();
      }
      form.classList.add("was-validated");
    });
  });
});

/**
 * Handler to get input and modify it based on requirments
 *
 * Example: 1212131313 => 121-213-1313
 */
const inputPhone = document.getElementById("inputPhone");
inputPhone.addEventListener("input", (event) => {
  const value = event.target.value.replace(/\D/g, "").slice(0, 10);
  const formattedValue =
    value.length > 0
      ? `${value.slice(0, 3)}${
          value.length >= 4 ? "-" + value.slice(3, 6) : ""
        }${value.length >= 7 ? "-" + value.slice(6, 10) : ""}`
      : "";
  event.target.value = formattedValue;
});

/**
 * Handler to get input and modify it based on requirments
 *
 * Example: 111111111 => 111-11-1111
 */
const inputSSN = document.getElementById("SSN");
inputSSN.addEventListener("input", (event) => {
  const value = event.target.value.replace(/\D/g, "").slice(0, 9);
  const formattedValue =
    value.length > 0
      ? `${value.slice(0, 3)}${
          value.length >= 4 ? "-" + value.slice(3, 5) : ""
        }${value.length >= 6 ? "-" + value.slice(5, 9) : ""}`
      : "";
  event.target.value = formattedValue;
});

/**
 * Used to show/hide ssn numbers
 */
function toggleVisible() {
  let input = document.getElementById("SSN");
  let closedIcon = document.getElementById("closed-eye");
  let openIcon = document.getElementById("open-eye");

  if (input.type === "password") {
    input.type = "text";
    openIcon.style.display = "block";
    closedIcon.style.display = "none";
  } else {
    input.type = "password";
    openIcon.style.display = "none";
    closedIcon.style.display = "block";
  }
}
