// 发起请求得到用户数据
import request from './request'

export const deleteSwitch = (data) => {
  return request({
    url: '/delswitch',
    method: 'post',
    data
  })
}
