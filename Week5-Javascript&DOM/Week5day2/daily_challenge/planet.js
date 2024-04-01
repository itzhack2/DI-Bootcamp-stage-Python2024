const planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"];
function getRandomColor() {
    const letters = '0123456789ABCDEF';
    let color = '#';
    for (let i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
}
function createPlanet(name, color) {
    const planetDiv = document.createElement("div");
    planetDiv.classList.add("planet");
    planetDiv.textContent = name;
    planetDiv.style.backgroundColor = color;
    return planetDiv;
}

function createMoons(planetDiv, numMoons) {
    for (let i = 0; i < numMoons; i++) {
        const moonDiv = document.createElement("div");
        moonDiv.classList.add("moon");
        moonDiv.textContent = `Moon ${i + 1}`;
        moonDiv.style.left = `${Math.random() * 80}px`; 
        moonDiv.style.top = `${Math.random() * 80}px`; 
        planetDiv.appendChild(moonDiv);
    }
}
// Function to create planets and moons
function createPlanetsAndMoons() {
    const section = document.querySelector(".listPlanets");
    planets.forEach(planet => {
        const color = getRandomColor();
        const planetDiv = createPlanet(planet, color);
        const numMoons = Math.floor(Math.random() * 5) + 1;
        createMoons(planetDiv, numMoons);
        section.appendChild(planetDiv);
    });
}
createPlanetsAndMoons();
