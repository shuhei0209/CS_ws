// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from utilities:srv/StringCommand.idl
// generated code does not contain a copyright notice

#ifndef UTILITIES__SRV__DETAIL__STRING_COMMAND__TRAITS_HPP_
#define UTILITIES__SRV__DETAIL__STRING_COMMAND__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "utilities/srv/detail/string_command__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace utilities
{

namespace srv
{

inline void to_flow_style_yaml(
  const StringCommand_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: command
  {
    out << "command: ";
    rosidl_generator_traits::value_to_yaml(msg.command, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const StringCommand_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: command
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "command: ";
    rosidl_generator_traits::value_to_yaml(msg.command, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const StringCommand_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace utilities

namespace rosidl_generator_traits
{

[[deprecated("use utilities::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const utilities::srv::StringCommand_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  utilities::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use utilities::srv::to_yaml() instead")]]
inline std::string to_yaml(const utilities::srv::StringCommand_Request & msg)
{
  return utilities::srv::to_yaml(msg);
}

template<>
inline const char * data_type<utilities::srv::StringCommand_Request>()
{
  return "utilities::srv::StringCommand_Request";
}

template<>
inline const char * name<utilities::srv::StringCommand_Request>()
{
  return "utilities/srv/StringCommand_Request";
}

template<>
struct has_fixed_size<utilities::srv::StringCommand_Request>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<utilities::srv::StringCommand_Request>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<utilities::srv::StringCommand_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace utilities
{

namespace srv
{

inline void to_flow_style_yaml(
  const StringCommand_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: answer
  {
    out << "answer: ";
    rosidl_generator_traits::value_to_yaml(msg.answer, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const StringCommand_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: answer
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "answer: ";
    rosidl_generator_traits::value_to_yaml(msg.answer, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const StringCommand_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace utilities

namespace rosidl_generator_traits
{

[[deprecated("use utilities::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const utilities::srv::StringCommand_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  utilities::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use utilities::srv::to_yaml() instead")]]
inline std::string to_yaml(const utilities::srv::StringCommand_Response & msg)
{
  return utilities::srv::to_yaml(msg);
}

template<>
inline const char * data_type<utilities::srv::StringCommand_Response>()
{
  return "utilities::srv::StringCommand_Response";
}

template<>
inline const char * name<utilities::srv::StringCommand_Response>()
{
  return "utilities/srv/StringCommand_Response";
}

template<>
struct has_fixed_size<utilities::srv::StringCommand_Response>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<utilities::srv::StringCommand_Response>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<utilities::srv::StringCommand_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<utilities::srv::StringCommand>()
{
  return "utilities::srv::StringCommand";
}

template<>
inline const char * name<utilities::srv::StringCommand>()
{
  return "utilities/srv/StringCommand";
}

template<>
struct has_fixed_size<utilities::srv::StringCommand>
  : std::integral_constant<
    bool,
    has_fixed_size<utilities::srv::StringCommand_Request>::value &&
    has_fixed_size<utilities::srv::StringCommand_Response>::value
  >
{
};

template<>
struct has_bounded_size<utilities::srv::StringCommand>
  : std::integral_constant<
    bool,
    has_bounded_size<utilities::srv::StringCommand_Request>::value &&
    has_bounded_size<utilities::srv::StringCommand_Response>::value
  >
{
};

template<>
struct is_service<utilities::srv::StringCommand>
  : std::true_type
{
};

template<>
struct is_service_request<utilities::srv::StringCommand_Request>
  : std::true_type
{
};

template<>
struct is_service_response<utilities::srv::StringCommand_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // UTILITIES__SRV__DETAIL__STRING_COMMAND__TRAITS_HPP_
