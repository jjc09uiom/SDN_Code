import request from './request'

export const delhost = (data) => {
  return request({
    url: '/delhost',
    method: 'post',
    data
  })
}
