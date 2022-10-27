const tween = KUTE.fromTo(
  "#mainBlob-1-1",
  { path: "#mainBlob-1-1" },
  { path: "#mainBlob-1-2" },
  { repeat: 999, duration: 4000, yoyo: true }
);

const tween1 = KUTE.fromTo(
  "#mainBlob-2-1",
  { path: "#mainBlob-2-1" },
  { path: "#mainBlob-2-2" },
  { repeat: 999, duration: 3000, yoyo: true }
);

tween.start();
tween1.start();
