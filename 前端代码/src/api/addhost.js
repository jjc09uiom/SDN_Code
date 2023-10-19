import request from './request'

export const addhost = (data) => {
  return request({
    url: '/addhost',
    method: 'post',
    data
  })
}
