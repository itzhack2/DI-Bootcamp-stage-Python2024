// Daily Challenge : Creating Objects
class Video {
    constructor(title, uploader, time) {
        this.title = title;
        this.uploader = uploader;
        this.time = time;
    }
    watch() {
        console.log(`${this.uploader} watched all ${this.time} seconds of ${this.title}!`);
    }
}
const video1 = new Video("Title1", "Uploader1", 120);
video1.watch();
const video2 = new Video("Title2", "Uploader2", 180);
video2.watch();
// Bonus:
const videosData = [
    { title: "Title1", uploader: "Uploader1", time: 120 },
    { title: "Title2", uploader: "Uploader2", time: 180 },
    { title: "Title3", uploader: "Uploader3", time: 150 },
    { title: "Title4", uploader: "Uploader4", time: 200 },
    { title: "Title5", uploader: "Uploader5", time: 90 }
];

// Bonus:
const videos = [];
videosData.forEach(videoData => {
    const { title, uploader, time } = videoData;
    const video = new Video(title, uploader, time);
    videos.push(video);
});

// Test
videos.forEach(video => {
    video.watch();
});
