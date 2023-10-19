import request from './request'

export const addlink = (data) => {
  return request({
    url: '/addlink',
    method: 'post',
    data
  })
}
