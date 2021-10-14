export function asyncDebounce(func, wait) {
  let timeout;
  return (...args) => {
    clearTimeout(timeout);
    return new Promise((resolve) => {
      timeout = setTimeout(() => resolve(func(...args)), wait);
    });
  };
}