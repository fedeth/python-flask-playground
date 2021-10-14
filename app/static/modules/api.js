export async function getStores(text, limit = false, offset = 0) {
  const relative_url = 'search?'
  const params = new URLSearchParams({text, limit, offset})
  const response = await fetch(relative_url + params)
  const stores = await response.json()
  return stores
}