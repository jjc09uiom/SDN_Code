// 发起请求得到用户数据
import request from './request'

export const getswitch = (params) => {
  return request({
    url: '/switch',
    method: 'GET',
    params
  })
}

// export const deleteClassDetails = (id) => {
//   return request({
//     url: `switchDetails/${id}`,
//     method: 'delete'
//   })
// }
