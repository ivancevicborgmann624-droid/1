
const CACHE_NAME = 'mlp-app-v1';
const ASSETS = [
  './',
  './index_enhanced.html',
  './styles_enhanced.css',
  './manifest.json',
  './images/twilight.webp',
  './images/rainbow.webp',
  './images/applejack.webp',
  './images/rarity.webp',
  './images/fluttershy.webp',
  './images/pinkie.webp'
];

// 安装Service Worker并缓存资源
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then((cache) => {
        console.log('Opened cache');
        return cache.addAll(ASSETS);
      })
  );
});

// 拦截请求并从缓存中提供资源
self.addEventListener('fetch', (event) => {
  event.respondWith(
    caches.match(event.request)
      .then((response) => {
        // 如果缓存中有，返回缓存的资源
        if (response) {
          return response;
        }
        // 否则从网络获取
        return fetch(event.request);
      })
  );
});

// 更新Service Worker
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((cacheNames) => {
      return Promise.all(
        cacheNames.map((cacheName) => {
          if (cacheName !== CACHE_NAME) {
            return caches.delete(cacheName);
          }
        })
      );
    })
  );
});
