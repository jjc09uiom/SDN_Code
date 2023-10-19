import request from './request'

export const addflow = (data) => {
  return request({
    url: '/addflow',
    method: 'post',
    data
  })
}
