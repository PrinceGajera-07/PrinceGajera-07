const fs = require('fs');
const path = require('path');

module.exports = (req, res) => {
  const games = [
    'acrade-contributions bomberman.svg',
    'acrade-contributions breakout.svg',
    'acrade-contributions galaga.svg',
    'acrade-contributions minesweeper.svg',
    'acrade-contributions pacman.svg',
    'acrade-contributions puzzle bobble.svg'
  ];

  const randomGame = games[Math.floor(Math.random() * games.length)];
  const filePath = path.join(process.cwd(), 'ready to go', randomGame);

  try {
    const svgData = fs.readFileSync(filePath, 'utf8');
    res.setHeader('Content-Type', 'image/svg+xml');
    res.setHeader('Cache-Control', 'no-cache, no-store, must-revalidate, max-age=0');
    res.setHeader('Pragma', 'no-cache');
    res.setHeader('Expires', '0');
    res.status(200).send(svgData);
  } catch (err) {
    res.status(500).send('Error loading arcade contribution SVG');
  }
};
