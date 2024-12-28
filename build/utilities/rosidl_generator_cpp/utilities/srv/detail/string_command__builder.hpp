// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from utilities:srv/StringCommand.idl
// generated code does not contain a copyright notice

#ifndef UTILITIES__SRV__DETAIL__STRING_COMMAND__BUILDER_HPP_
#define UTILITIES__SRV__DETAIL__STRING_COMMAND__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "utilities/srv/detail/string_command__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace utilities
{

namespace srv
{

namespace builder
{

class Init_StringCommand_Request_command
{
public:
  Init_StringCommand_Request_command()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::utilities::srv::StringCommand_Request command(::utilities::srv::StringCommand_Request::_command_type arg)
  {
    msg_.command = std::move(arg);
    return std::move(msg_);
  }

private:
  ::utilities::srv::StringCommand_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::utilities::srv::StringCommand_Request>()
{
  return utilities::srv::builder::Init_StringCommand_Request_command();
}

}  // namespace utilities


namespace utilities
{

namespace srv
{

namespace builder
{

class Init_StringCommand_Response_answer
{
public:
  Init_StringCommand_Response_answer()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::utilities::srv::StringCommand_Response answer(::utilities::srv::StringCommand_Response::_answer_type arg)
  {
    msg_.answer = std::move(arg);
    return std::move(msg_);
  }

private:
  ::utilities::srv::StringCommand_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::utilities::srv::StringCommand_Response>()
{
  return utilities::srv::builder::Init_StringCommand_Response_answer();
}

}  // namespace utilities

#endif  // UTILITIES__SRV__DETAIL__STRING_COMMAND__BUILDER_HPP_
