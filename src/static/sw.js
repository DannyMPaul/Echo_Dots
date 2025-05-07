const CACHE_NAME = 'morse-braille-translator-v1';
const ASSETS_TO_CACHE = [
    '/',
    '/static/manifest.json',
    '/static/sw.js'
];

self.addEventListener('install', (event) => {
    event.waitUntil(
        caches.open(CACHE_NAME)
            .then((cache) => cache.addAll(ASSETS_TO_CACHE))
    );
});

self.addEventListener('fetch', (event) => {
    event.respondWith(
        fetch(event.request)
            .catch(() => caches.match(event.request))
    );
});