import request from './request'

export const addswitch = (data) => {
  return request({
    url: '/addswitch',
    method: 'post',
    data
  })
}
