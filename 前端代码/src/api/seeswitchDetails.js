// 发起请求得到用户数据
import request from './request'

export const getswitchDetails = (id) => {
  return request({
    url: `switch/${id}`,
    method: 'GET'
  })
}
// export const getswitchDetails = (data) => {
//   return request({
//     url: '/switch',
//     method: 'GET',
//     data
//   })
// }
// export const deleteClassDetails = (id) => {
//   return request({
//     url: `switchDetails/${id}`,
//     method: 'delete'
//   })
// }
