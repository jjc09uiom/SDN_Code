import request from './request'

export const dellink = (data) => {
  return request({
    url: '/dellink',
    method: 'post',
    data
  })
}
