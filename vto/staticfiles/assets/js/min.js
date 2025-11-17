document.addEventListener("DOMContentLoaded", () => {
  const words = [
    "an Engineer",
    "a Web Developer",
    "a Project Manager",
    "a Content Specialist",
    "an HSE Expert",
    "a Data Analyst",
    "a Cloud Engineer",
    "a Fintech Developer",
    "a UX/UI Designer",
    "a Technical Writer"
  ];

  let wordIndex = 0;
  let charIndex = 0;
  let isDeleting = false;
  const typingSpeed = 100;
  const deletingSpeed = 60;
  const delayBetweenWords = 1500;
  const typewriter = document.querySelector(".typewriter");

  function type() {
    if (!typewriter) return;

    const currentWord = words[wordIndex];
    const visibleText = currentWord.substring(0, charIndex);

    typewriter.textContent = visibleText;

    if (!isDeleting && charIndex < currentWord.length) {
      // keep typing
      charIndex++;
      setTimeout(type, typingSpeed);
    } else if (!isDeleting && charIndex === currentWord.length) {
      // word fully typed — wait a bit before deleting
      isDeleting = true;
      setTimeout(type, delayBetweenWords);
    } else if (isDeleting && charIndex > 0) {
      // deleting characters
      charIndex--;
      setTimeout(type, deletingSpeed);
    } else {
      // done deleting — move to next word
      isDeleting = false;
      wordIndex = (wordIndex + 1) % words.length;
      setTimeout(type, 300);
    }
  }

  type();
});
