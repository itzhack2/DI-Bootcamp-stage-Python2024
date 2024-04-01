document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('libform');
    const storySpan = document.getElementById('story');
    const shuffleButton = document.getElementById('shuffle-button');
    form.addEventListener('submit', function(event) {
      event.preventDefault();
      // Get values from input fields
      const noun = document.getElementById('noun').value.trim();
      const adjective = document.getElementById('adjective').value.trim();
      const person = document.getElementById('person').value.trim();
      const verb = document.getElementById('verb').value.trim();
      const place = document.getElementById('place').value.trim();
      // Check if any input is empty
      if (noun === '' || adjective === '' || person === '' || verb === '' || place === '') {
        alert('Please fill in all the fields!');
        return;
      }
      // Generate story using the values
      const story = `Once upon a time, there was a ${adjective} ${noun} named ${person}. 
      ${person} loved to ${verb} in ${place}.`;
  
      // Display the story
      storySpan.textContent = story;
    });
    // Array of possible stories
    const stories = [
      'Once upon a time, there was a {adjective} {noun} named {person}. {person} loved to {verb} in {place}.',
      '{person} found a {adjective} {noun} in {place}. {person} decided to {verb} it.',
      'In a {place} far far away, there lived a {adjective} {noun} named {person}. {person} always wanted to {verb}.'
    ];

    // Shuffle function to shuffle the stories array
    function shuffle(array) {
      for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
      }
    }

    // Event listener for shuffle button
    shuffleButton.addEventListener('click', function() {
      shuffle(stories);
      const storyIndex = Math.floor(Math.random() * stories.length);
      const shuffledStory = stories[storyIndex].replace(/{noun}/g, noun)
        .replace(/{adjective}/g, adjective)
        .replace(/{person}/g, person)
        .replace(/{verb}/g, verb)
        .replace(/{place}/g, place);
      storySpan.textContent = shuffledStory;
    });
  });
  