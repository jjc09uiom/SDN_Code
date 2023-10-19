import request from './request'

export const delflow = (data) => {
  return request({
    url: '/delflow',
    method: 'delete',
    data
  })
}
